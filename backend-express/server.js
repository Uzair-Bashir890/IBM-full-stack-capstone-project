const express = require('express');
const mongoose = require('mongoose');
const bodyParser = require('body-parser');
const cors = require('cors');
const app = express();
app.use(cors());
app.use(bodyParser.json());


const dealersController = require('./controllers/dealers');


// Connect to MongoDB (local default)
mongoose.connect(process.env.MONGO_URI || 'mongodb://127.0.0.1:27017/dealers_db', {
useNewUrlParser: true,
useUnifiedTopology: true
});


// Routes
app.get('/api/dealers', dealersController.getAll);
app.get('/api/dealers/:id', dealersController.getById);
app.get('/api/dealers/:id/reviews', dealersController.getReviews);
app.post('/api/dealers/:id/reviews', dealersController.addReview);
app.get('/api/dealers-by-state', dealersController.getByState);


const port = process.env.PORT || 3000;
app.listen(port, () => console.log('Express server running on', port));