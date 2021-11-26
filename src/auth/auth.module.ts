import { MongooseModule } from '@nestjs/mongoose';


import { ConfigModule } from '@nestjs/config';

// import { LocalStrategy } from './local.strategy';
// import { UserService } from './../../services/user.service';
// import { User } from './../../models/user.entity';
import { TypeOrmModule } from '@nestjs/typeorm';
// import { AuthController } from './auth.controller';
import { Module } from '@nestjs/common';
import { PassportModule } from '@nestjs/passport';
import { JwtModule } from '@nestjs/jwt';
import { AuthController } from './auth.controller';

import { LocalStrategy } from './local.strategy';
import { JwtStrategy } from './jwt.trategy';
import { UserService } from 'src/user/User.service';
import { userSchema } from 'src/user/User.model';


@Module({
  imports: [
    PassportModule,
    ConfigModule.forRoot(),
    MongooseModule.forFeature([{name: 'Users', schema: userSchema}]),
    JwtModule.register({
      secret: process.env.JWT_SECRET,
      signOptions: {
        expiresIn: 60 * 30,
      },
    }),
    MongooseModule.forFeature([{name: 'Users', schema: userSchema}]),
  ],
  providers: [JwtStrategy,UserService,LocalStrategy],
  controllers: [AuthController],
})
export class AuthModule {}
