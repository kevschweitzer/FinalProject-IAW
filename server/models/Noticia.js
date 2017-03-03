var mongoose = require('mongoose');
var Schema   = mongoose.Schema;

// Create the MovieSchema.
var NoticiaSchema = new mongoose.Schema({
  titulo: {
    type: String,
    required: true,
  },
  url: {
    type: String,
    required: true
  }
});

// Export the model.
module.exports = mongoose.model('noticia', NoticiaSchema);
