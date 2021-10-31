import { Controller, Get, Render, Req } from '@nestjs/common';
import { PersonService } from './person.service';


@Controller('home')
export class PersonController {
  constructor(private readonly personService: PersonService) {}

    @Get()
    @Render('intro/index')
    async index() {
      var person = await this.personService.getPersons();
      var a = person;
      console.log(person);
    }
    @Get()
    async getAll(){

    }
    
    
}
