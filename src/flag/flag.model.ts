

import * as mongoose from 'mongoose';




export const Flagschema = new mongoose.Schema({

  Flagcheck:   Boolean,
}
);
export interface Flag  extends mongoose.Document {
    Flagcheck:   Boolean,
}



