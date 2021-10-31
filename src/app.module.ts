
import { MongooseModule } from '@nestjs/mongoose';
import { Module } from '@nestjs/common';
import { AppController } from './app.controller';
import { AppService } from './app.service';
import { PersonModule } from './persons/person.module';
import { TurnModule } from './turns/turn.module';



@Module({
  imports: [MongooseModule.forRoot('mongodb+srv://hda1010:duyanh123@cluster0.ukowb.mongodb.net/facerecognition?retryWrites=true&w=majority'),PersonModule,TurnModule],
  controllers: [AppController],  
  providers: [AppService],
})
export class AppModule {}
