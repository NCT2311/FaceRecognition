

import * as mongoose from 'mongoose';



export const Userschema = new mongoose.Schema({
  Fname:  String, // String is shorthand for {type: String}
  Lname: String,
  body:   String,
  urlimg:   String,
  AccountName: String,
  password: String,
  createAt: { type: Date, default: Date.now },
  updateAt: { type: Date, default: Date.now },
  gender: Boolean,

});



