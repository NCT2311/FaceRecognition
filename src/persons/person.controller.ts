import { Controller, Get, Post, Render, Req, UseGuards } from '@nestjs/common';
import { AuthGuard } from '@nestjs/passport';
import { TurnService } from 'src/turns/turn.service';
import { PersonService } from './person.service';


@Controller('home')
export class PersonController {
  constructor(private readonly personService: PersonService , private readonly turnService: TurnService) {}

    @Get()
    @Render('new')
    async index() {
      // var person = await this.personService.getPersons();
      // var a = person;
      // console.log(person);
    }
}
