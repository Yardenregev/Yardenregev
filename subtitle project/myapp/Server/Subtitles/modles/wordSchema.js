import mongoose from 'mongoose';

const wordSchema = mongoose.Schema({
    id:Number,
    value:String, 
    is_term : String,
    time_stamp : Date,
    search : String,
});

const WordType = mongoose.model('WordType',wordSchema);

export default WordType;