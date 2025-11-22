const Dealer = require('../models/dealer');


exports.getAll = async (req, res) => {
const dealers = await Dealer.find();
res.json(dealers);
};


exports.getById = async (req, res) => {
const d = await Dealer.findById(req.params.id);
if (!d) return res.status(404).json({error: 'Not found'});
res.json(d);
};


exports.getByState = async (req, res) => {
const state = req.query.state;
const dealers = await Dealer.find({ state: state });
res.json(dealers);
};


exports.getReviews = async (req, res) => {
const id = req.params.id;
const dealer = await Dealer.findById(id);
if (!dealer) return res.status(404).json({error:'Not found'});
res.json(dealer.reviews);
};


exports.addReview = async (req, res) => {
const id = req.params.id;
const { name, review, sentiment } = req.body;
const dealer = await Dealer.findById(id);
if (!dealer) return res.status(404).json({error:'Not found'});
dealer.reviews.push({ name, review, sentiment });
await dealer.save();
res.json({ success: true, review: dealer.reviews[dealer.reviews.length-1] });
};