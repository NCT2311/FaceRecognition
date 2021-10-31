

import * as mongoose from 'mongoose';




export const Personschema = new mongoose.Schema({
  id: Number,
  Fname:  String, // String is shorthand for {type: String}
  Lname: String,
  Status:   Boolean,
  createAt: { type: Date, default: Date.now },
  updateAt: { type: Date, default: Date.now },
  
}
);
export interface Person {
        id: Number;
        Fname: string;
        Lname: string;
        Status: Boolean;
        createAt: Date;
        updateAt: Date;
}



