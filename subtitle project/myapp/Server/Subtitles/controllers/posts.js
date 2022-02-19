import WordType from "../modles/wordSchema.js";

export const getPosts = async (req, res) => {
try {
    const postwords = await WordType.find();
    res.status(200).json(postwords);
} catch (error) {
    res.status(404).json({ message: error.message });
}}

export const createPost = async (req, res) => {
    const body = req.body;

    const new_post = new WordType(body)
    try {
       await new_post.save();
       res.status(201).json(new_post);
    } catch (error) {
        res.status(404).json({ message: error.message });
    }
}