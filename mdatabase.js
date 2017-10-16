
/*Initiates a User schema and exports it 
*/

var mongoose = require('mongoose');
//var GeoJson = require('mongoose-geojson-schema');
var Schema = mongoose.Schema;

var boardSchema = new Schema({
  name: String,
  longitude: Number,
  latitude: Number,
  token: String,
  publicVisable: Boolean, 
  posts: [
    {
      title: String, 
      authID: String, 
      authName: String, 
      dateCreated: Number, 
      dateEdited: Number,
      content: {
        textBody: String, 
        imageBody: String,
      } 

    }
  ]

});

var Board = mongoose.model('Board', BoardSchema);

module.exports = {
  Board: Board
}