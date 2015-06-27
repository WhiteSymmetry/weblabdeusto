Blockly.Blocks['romie_move_forward'] = {
	init: function() {
		this.setHelpUrl(null);
		this.setColour(65);
		this.appendDummyInput()
			.appendField("Ir recto");
		this.setPreviousStatement(true, "null");
		this.setNextStatement(true, "null");
		this.setTooltip('');
	}
};

Blockly.Blocks['romie_turn_left'] = {
	init: function() {
		this.setHelpUrl(null);
		this.setColour(65);
		this.appendDummyInput()
			.appendField("Girar a la izquierda");
		this.setPreviousStatement(true, "null");
		this.setNextStatement(true, "null");
		this.setTooltip('');
	}
};

Blockly.Blocks['romie_turn_right'] = {
	init: function() {
		this.setHelpUrl(null);
		this.setColour(65);
		this.appendDummyInput()
			.appendField("Girar a la derecha");
		this.setPreviousStatement(true, "null");
		this.setNextStatement(true, "null");
		this.setTooltip('');
	}
};

Blockly.JavaScript['romie_move_forward'] = function(block) {
	code = 'forward();\n'+
			'while(isMoving());\n';
	return code;
};

Blockly.JavaScript['romie_turn_left'] = function(block) {
	code = 'left();\n'+
			'while(isMoving());\n';
	return code;
};

Blockly.JavaScript['romie_turn_right'] = function(block) {
	code = 'right();\n'+
			'while(isMoving());\n';
	return code;
};
