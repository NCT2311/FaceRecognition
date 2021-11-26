import { NestFactory } from '@nestjs/core';
import { join } from 'path';
import { AppModule } from './app.module';
import { NestExpressApplication } from '@nestjs/platform-express';
import * as moment from 'moment';
import * as session from "express-session";
import * as cookieParser from 'cookie-parser';
async function bootstrap() {
  const app = await NestFactory.create<NestExpressApplication>(AppModule);
  app.useStaticAssets(join(__dirname, '..', 'public'));
  app.setBaseViewsDir(join(__dirname, '..', 'views'));
  app.setViewEngine('pug');
  moment.locale('en');
  app.use(cookieParser());
  app.use(
    session({
      secret: process.env["SESSION_SECRET"],
      resave: false,
      saveUninitialized: false,
    })
  );
  app.setLocal("moment", moment);
  await app.listen(3000);
}
bootstrap();
