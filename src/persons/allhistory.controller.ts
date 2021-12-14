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
import { TurnService } from 'src/turns/turn.service';
import { PersonService } from './person.service';

@Controller('alldata')
@UseGuards(AuthGuard('jwt'))
export class AllhistoryController {
  constructor(
    private readonly personService: PersonService,
    private readonly turnService: TurnService,
  ) { }

  @Get()
  @UseGuards(AuthGuard('jwt'))
  @Render('alldata/index')
  async index() {
    var list = await this.turnService.getTurns();
    var people = await this.personService.getPersons();
    for (var i = 0; i < list.length; i++) {
      for (var j = 0; j < people.length; j++) {
        if (!list[i].Response) list[i].Response = false;
        if (list[i].Personid.toString() == people[j].id) {
          if (people[j].Fname == "" && people[j].Lname == "") {
            people[j].Fname = 'Unidentified';
            people[j].Lname = 'Unidentified';
          }
          var neww = {
            id: list[i].id,
            urlimg: list[i].urlimg,
            Personid: list[i].Personid,
            Status: list[i].Status,
            Response: list[i].Response,
            CreateAt: list[i].CreateAt,
            Fname: people[j].Fname,
            Lname: people[j].Lname,
          };
          list[i] = neww;
        }
      }
    }
    for (var i = 0; i < list.length; i++) {
      if (!list[i]['Fname'] && !list[i]['Lname']) {
        var neww2 = {
          id: list[i].id,
          urlimg: list[i].urlimg,
          Personid: list[i].Personid,
          Status: list[i].Status,
          Response: list[i].Response,
          CreateAt: list[i].CreateAt,
          Fname: 'Unidentified',
          Lname: 'Unidentified',
        };
        list[i] = neww2;
      }
    }
    return {
      list: list,
    };
  }
}