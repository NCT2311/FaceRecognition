import { Body, Controller, Get, Post, Render, Req, UseGuards } from '@nestjs/common';
import { AuthGuard } from '@nestjs/passport';
import { TurnService } from 'src/turns/turn.service';
import { Person } from './person.model';
import { PersonService } from './person.service';


@Controller('history')
@UseGuards(AuthGuard('jwt'))
export class HistoryController {
  constructor(private readonly personService: PersonService , private readonly turnService: TurnService) {}

    @Get()
    @UseGuards(AuthGuard('jwt'))
    @Render('history/index')
    async index() {
        var list =  await this.personService.getPersons();
        var data = new Array();
        for (var i = 0 ; i < list.length ; i++){
          if(list[i].Status == true){
            data.push(list[i]);
          }
        }
        return {
          list: data,
    }
  }
  @Post('/getallTurn')
  @UseGuards(AuthGuard('jwt'))
  async getdata2(@Body('id') id: string) { 
    var list =  await this.turnService.getbyPersonID(id);
    return {
        list:list
  }
}
}
