var mongoose = require('mongoose');
var Schema   = mongoose.Schema;

// Create the NoticiaSchema.
var NoticiaSchema = new mongoose.Schema({
  titulo: {
    type: String,
    required: true
  },
  url: {
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
