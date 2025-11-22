const mongoose = require('mongoose');
const Schema = mongoose.Schema;


const ReviewSchema = new Schema({
name: String,
review: String,
sentiment: String,
created_at: { type: Date, default: Date.now }
});


const DealerSchema = new Schema({
name: String,
city: String,
state: String,
address: String,
full_name: String,
reviews: [ReviewSchema]
});


module.exports = mongoose.model('Dealer', DealerSchema);