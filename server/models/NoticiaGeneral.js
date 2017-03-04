var mongoose = require('mongoose');
var Schema   = mongoose.Schema;

// Create the NoticiaGeneralSchema.
var NoticiaGeneralSchema = new mongoose.Schema({
    titulo: {
      type: String,
      required: true
    },
    noticias: [{
      type: String,  //Arreglo de id's de las noticias relacionadas.
      required: true
    }]

});

// Export the model.
module.exports = mongoose.model('noticiaGeneral', NoticiaGeneralSchema);
