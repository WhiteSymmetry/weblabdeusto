// From StackOverflow. To extract parameters from the URL (not the hash)
(function ($) {
    $.QueryString = (function (a) {
        if (a == "") return {};
        var b = {};
        for (var i = 0; i < a.length; ++i) {
            var p = a[i].split('=');
            if (p.length != 2) continue;
            b[p[0]] = decodeURIComponent(p[1].replace(/\+/g, " "));
        }
        return b;
    })(window.location.search.substr(1).split('&'))
})(jQuery);

///////////////////////////////////////////////////////////////
//
// WeblabExp is a library that provides a simple way to interact
// with Weblab experiments.
//
// It relies on jQuery-style deferred callbacks, and is thus
// dependent on the jQuery library.
//
// DEPENDENCIES: jQuery
//
///////////////////////////////////////////////////////////////
WeblabExp = new function () {

    ///////////////////////////////////////////////////////////////
    //
    // PRIVATE ATTRIBUTES AND FUNCTIONS
    // The API uses these internally to provide an easier to use,
    // higher level API. Users of this class do not need to be
    // aware of them.
    //
    ///////////////////////////////////////////////////////////////

    var mTargetURL;
    var mReservation;

    var mStartHandlers = [];
    var mFinishHandlers = [];

    //! Extracts the reservation id from the URL (in the hash).
    //!
    //! @return The reservation ID if present in the URL's hash field, or undefined.
    this._extractReservation = function () {
        mReservation = $.QueryString["reservation"];
    };

    //! Extracts the targeturl from the URL (in the hash). This is the URL towards which
    //! the AJAX requests will be directed. If not specified through the URL, then
    //! it will use a default (<location>/weblab/json/).
    this._extractTargetURL = function () {
        mTargetURL = $.QueryString["targeturl"];
        if (mTargetURL == undefined)
            mTargetURL = document.location.origin + "/weblab/json/";
    };


    //! Gets the reservation that Weblab is using.
    //!
    //! @return The reservation ID.
    this._getReservation = function () {
        return mReservation;
    };

    //! Gets the TargetURL that we are using.
    //!
    //! @return The target URL.
    this._getTargetURL = function () {
        return mTargetURL;
    };

    this._setTargetURL = function (targetURL) {
        mTargetURL = targetURL;
    };

    this._setReservation = function (reservation) {
        mReservation = reservation;
    };

    this._poll = function () {
        var promise = $.Deferred();
        var request = {"method": "poll", "params": {"reservation_id": {"id": mReservation}}};

        this._send(request)
            .done(function (success) {
                console.log("Data received: " + success);
                console.log(success);
                promise.resolve(success);
            })
            .fail(function (error) {
                promise.reject(error);
            });

        return promise.promise();
    }; //!_poll


    /**
     * Internal send function. It will send the request to the target URL.
     * Meant only for internal use. If an error occurs (network error, "is_exception" to true, or other) then
     * the exception will be printed to console, and nothing else will happen (as of now).
     *
     * @param request: The JSON-able to send. This method will not check whether the format of the JSON-able is
     * right or not. It is assumed it is. This should be a JSON-able object and NOT a JSON string.
     *
     * @return: Promise, whose .done(result_field) or .fail will be invoked depending on the success of the request.
     *
     */
    this._send = function (request) {

        var promise = $.Deferred();

        if (typeof(request) !== 'object') {
            console.error("[_SEND]: Request parameter should be an object.");
            return;
        }

        $.ajax({
            "type": "POST",
            "url": mTargetURL,
            "data": JSON.stringify(request),
            "dataType": "json",
            "contentType": "application/json"
        })
            .done(function (success, status, jqXHR) {
                // Example of a response: {"params":{"reservation_id":{"id":"2da9363c-c5c4-4905-9f22-817cbdf1e397;2da9363c-c5c4-4905-9f22-817cbdf1e397.default-route-to-server"}}, "method":"get_reservation_status"}

                // Check that the internal is_exception is set to false.
                if (success["is_exception"] === true) {

                    console.error("[ERROR][_send]: Returned exception (is_exception is true)");
                    console.error(success);

                    promise.reject(success);
                    return;
                }

                var result = success["result"];

                if (result == undefined) {
                    console.error("[ERROR][_send]: Response didn't contain the expected 'result' key.");
                    console.error(success);

                    promise.reject(success);
                    return;
                }

                // The request, whatever it contains, was apparently successful. We call the success handler, passing
                // the result field.
                promise.resolve(result, status, jqXHR);
            })
            .fail(function (fail) {
                console.error("[ERROR][_send]: Could not carry out the POST request to the target URL: " + targetURL);
                console.error(fail);

                promise.reject(fail);
            });

        return promise;

    }; // !_send

    //! Internal method to check the reservation status. While the experiment is active this should return confirmed.
    //! As of now that is in fact the only supported response, because the full reservation process is not covered
    //! by this API.
    this._get_reservation_status = function () {
        var request = {"method": "get_reservation_status", "params": {"reservation_id": {"id": mReservation}}};

        this._send(request, function (success_data) {
            // Example of a response: {"params":{"reservation_id":{"id":"2da9363c-c5c4-4905-9f22-817cbdf1e397;2da9363c-c5c4-4905-9f22-817cbdf1e397.default-route-to-server"}}, "method":"get_reservation_status"}

            console.log("Data received: " + success_data);
            console.log(success_data);

            var result = success_data["result"];
            var status = result["status"];

            if (status != "Reservation::confirmed") {
                console.error("[ERROR][get_reservation_status]: Status is not Reservation::confirmed as was expected");
                return;
            }


            var time = result["time"];
            var initial_configuration = result["initial_configuration"];

            // Invoke the start handlers.
            for (var i = 0; i < mStartHandlers.length; i++) {
                console.log("Invoking start handler");
                mStartHandlers[i](initial_configuration, time);
            }

            // Remove the handlers so that they are not invoked again.
            mStartHandlers = [];
        });
    }; // !_get_reservation

    //! Internal method to send a command to the server.
    //!
    this._send_command = function (command, successHandler, errorHandler) {
        var request = {"method": "send_command", "params": {"command": {"commandstring": command}, "reservation_id": {"id": mReservation}}};

        this._send(request, function (success_data) {
            console.log("Data received: " + success_data);
            console.log(success_data);

            if (successHandler != undefined)
                successHandler(success_data);
        });
    }; // !_send_command

    this._finished_experiment = function (successHandler) {
        var request = {"method": "finished_experiment", "params": {"reservation_id": {"id": mReservation}}};

        this._send(request)
            .done(function (success_data) {
                console.log("Data received: " + success_data);
                console.log(success_data);

                // Invoke the finish handlers.
                for (var i = 0; i < mFinishHandlers; i++) {
                    mFinishHandlers[i]();
                }

                // Clear the finish handlers so that they are not invoked again.
                mFinishHandlers = [];

                if (successHandler != undefined)
                    successHandler(success_data);
            });
    };


    ///////////////////////////////////////////////////////////////
    //
    // PUBLIC INTERFACE
    // The following methods are part of the public interface of this
    // class. They can be used freely. Several of them rely on callbacks.
    // They might not work properly if they are run stand-alone, on a
    // context different than Weblab-Deusto.
    //
    ///////////////////////////////////////////////////////////////


    /**
     * Sends a command to the experiment server.
     * @param {str} command: The command to send.
     * @returns {$.Promise} Promise with done() and fail() callbacks.
     *
     * @example
     * this.sendCommand("TURN_LED ON")
     *   .done(function(result) {
     *      console.log("LED IS: " + result);
     *   })
     *   .fail(function(error) {
     *      console.log("Failed to turn LED ON". Cause: " + error);
     *   });
     */
    this.sendCommand = function (command) {

        var promise = $.Deferred();

        this._send_command(command, function (success) {
            promise.resolve(success);
        }, function (error) {
            promise.reject(error);
        });

        return promise.promise();
    };


    //! Sends a command to the experiment server and prints the result to console.
    //! If the command was successful it is printed to the stdout and otherwise to stderr.
    //!
    //! @param text: Command to send.

    /**
     * Sends a command to the experiment server and prints the result to the console.
     * If the command was successful it will be printed to stdout and otherwise it
     * will be printed to stderr.
     *
     * @param {str} command: Command to send.
     * @returns {$.Promise} Promise with .done() and .fail() callbacks. Making use of it is optional.
     *
     * @example
     *  this.testCommand("TURN_LED ON");
     */
    this.testCommand = function (command) {

        var promise = $.Deferred();

        this.sendCommand(command)
            .done(function (success) {
                console.log("SUCCESS: " + success);
                promise.resolve(success);
            })
            .fail(function (error) {
                console.error("ERROR: " + error);
                promise.reject(error);
            });

        return promise.promise();
    };


    /**
     * Finishes the experiment.
     *
     * @returns {$.Promise} Promise with .done and .fail callbacks.
     *
     * TODO: .fail not yet supported.
     */
    this.finishExperiment = function () {

        var promise = $.Deferred();

        this._finished_experiment(function (success) {
            promise.resolve(success);
        });

        return promise.promise();
    };

    //! addStartHandler(startHandler(initialConfiguration, timeLeft))
    //!
    //! Registers a start handler, which will be called when the experiment's interaction starts. Several start
    //! handlers can be registered. They will be invoked in the order they are registered.
    //!
    //! @param startHandler: The start handler function. Should receive the starting configuration and the time left.
    this.addStartHandler = function (startHandler) {
        mStartHandlers.push(startHandler);
    };

    //! addFinishHandler(finishHandler(reason))
    //!
    //! Registers a finish handler, which will be called when the experiment finishes. Several end handlers can be
    //! registered. They will be invoked in the order they are registered.
    //!
    //! @param finishHandler: The finish handler function. Should receive an object related to the cause, whose
    //! exact nature is for now not specified.
    this.addFinishHandler = function (finishHandler) {
        mFinishHandlers.push(finishHandler);
    };


    //! Indicates that we are ready and that we have registered all callbacks.
    //! Should be called to start.
    this.ready = function () {
        this._get_reservation_status();


        // Poll every minute.
        function poller() {
            this._poll()
                .done(function () {
                    window.setTimeout(poller.bind(this), 1000 * 30);
                }.bind(this));
        };
        window.setTimeout(poller.bind(this), 1000 * 30);
    };


    ///////////////////////////////////////////////////////////////
    //
    // CONSTRUCTOR
    // The following is internal code to create the object.
    //
    ///////////////////////////////////////////////////////////////

    // Extract the reservation id from the hash.
    this._extractReservation();

    // Extract the target URL from the hash or set a default one.
    this._extractTargetURL();

    //$.cookie("weblabsessionid", "T-Go5baSwSB3SHsO.route2");

}; // !WeblabExp




