

import * as mongoose from 'mongoose';
import { Schema } from 'mongoose';

export const Turnschema = new mongoose.Schema({
  urlimg: String,
  Status:   Boolean,
  Personid: { type: Schema.Types.ObjectId, ref: 'Person' },
  createAt: { type: Date, default: Date.now },


});
export interface Turn {
         id: String;
        urlimg: String;
        Status: Boolean;
        Personid: { type: Schema.Types.ObjectId, ref: 'Person' };
        createAt: Date;

}



