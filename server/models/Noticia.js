var mongoose = require('mongoose');
var Schema   = mongoose.Schema;

// Create the NoticiaSchema.
var NoticiaSchema = new mongoose.Schema({
  titulo: {
    type: String,
    required: true
  },
  texto: {
    type: String,
    required: true
  },
  sentiment: {
    type: Number,
    required: true
  },
  imagenUrl: {
    type: String,
    required: true
  },
  diario: {         //id del diario al que pertenece la noticia
    type: String,
    required: true
  }
});

// Export the model.
module.exports = mongoose.model('noticia', NoticiaSchema);
