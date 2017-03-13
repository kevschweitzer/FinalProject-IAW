var mongoose = require('mongoose');
var Schema = mongoose.Schema;

//Create DiarioSchema

var DiarioSchema = new mongoose.Schema({

  nombre: {
    type: String,
    required: true
  },
  url: {
    type: String,
    required: true
  },
  logo: {
    type: String, //url de la imagen
    required: true
  }
});

//Export the model

module.exports = mongoose.model('diario', DiarioSchema);
