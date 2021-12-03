

import {
  Body,
  Controller,
  Get,
  Post,
  Render,
  Req,
  UseGuards,
} from '@nestjs/common';
import { AuthGuard } from '@nestjs/passport';
import { Turn } from 'src/turns/turn.model';
import { TurnService } from 'src/turns/turn.service';
import { PersonService } from './person.service';

@Controller('alldata')
@UseGuards(AuthGuard('jwt'))
export class AllhistoryController {
  myArray: any;
  constructor(
    private readonly personService: PersonService,
    private readonly turnService: TurnService,
  ) {}


  @Get()
  @UseGuards(AuthGuard('jwt'))
  @Render('alldata/index')
  async index() {
    var list = await this.turnService.getTurns();
    list.sort(function(a, b) {
      var dateA = new Date(a.CreateAt);
      var   dateB = new Date(b.CreateAt);
      return (dateB.getTime() - dateA.getTime())
   });
   
    return {
      list: list,
    }; 
  }

}
