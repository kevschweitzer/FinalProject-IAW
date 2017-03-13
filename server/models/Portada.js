var mongoose = require('mongoose');
var Schema   = mongoose.Schema;

// Create the NoticiaSchema.
var PortadaSchema = new mongoose.Schema({
  url: {
    type: String,
    required: true
  },
  titulo: {
    type: String,
    required: true
  },
  nombreDiario: {
    type: String,
    required: true
  }

});

// Export the model.
module.exports = mongoose.model('portada', PortadaSchema);
