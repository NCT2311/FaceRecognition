

import * as mongoose from 'mongoose';



export const userSchema = new mongoose.Schema({

  username:   String,
  password:   String,
  updateAt: { type: Date, default: Date.now },
}
);
export interface User  extends mongoose.Document {
    username:   string,
    password:   string,
    updateAt: Date;
}



