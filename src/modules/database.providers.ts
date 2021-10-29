import * as mongoose from 'mongoose';

const newLocal = 'mongodb+srv://hda1010:duyanh123@cluster0.ukowb.mongodb.net/facerecognition?retryWrites=true&w=majority';
export const databaseProviders = [
  {
    provide: 'DATABASE_CONNECTION',
    useFactory: (): Promise<typeof mongoose> =>
      mongoose.connect(newLocal),
  },
];