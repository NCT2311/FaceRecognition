
import { Connection } from 'mongoose';
import { Userschema } from 'src/models/user.schema';

export const userProviders = [
  {
    provide: 'USER_MODEL',
    useFactory: (connection: Connection) => connection.model('Userschema', Userschema),
    inject: ['DATABASE_CONNECTION'],
  },
];