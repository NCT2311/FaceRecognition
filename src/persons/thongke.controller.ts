import { Body, Controller, Get, Post, Render, Req, UseGuards } from '@nestjs/common';
import { AuthGuard } from '@nestjs/passport';
import { TurnService } from 'src/turns/turn.service';
import { PersonService } from './person.service';


@Controller('thongke')
export class ThongkeController {
  constructor(private readonly personService: PersonService , private readonly turnService: TurnService) {}

    @Get()
    @UseGuards(AuthGuard('jwt'))
    @Render('thongke/index')
    async index() {
      var dataturn = await this.turnService.getTurns();
      var totalofturn = dataturn.length;
      var today = new Date();
      var myToday = new Date(today.getFullYear(), today.getMonth(), today.getDate(), 0, 0, 0);
      //console.log(myToday);
      var totalinday=0;
      var totalla = 0;
      var totalquen = 0;
      for (var i = 0 ; i < dataturn.length ; i++) {
         if(dataturn[i].CreateAt > myToday){
            totalinday++;
            if(dataturn[i].Status == true){
                totalquen++;
            }
            else{
                totalla++;
            }
         }
      }
      var percentquen = Math.round(totalquen*100/totalofturn);
      var percentla = Math.round(totalla*100/totalofturn);
      return{
        totalofturn:totalofturn,
        totalinday:totalinday,
        totalla:totalla,
        totalquen:totalquen,
        percentquen:percentquen,
        percentla:percentla
      }
    }
    @Post('/getall')
    @UseGuards(AuthGuard('jwt'))
    async getdata2(@Body('id') id: string) { 
        var dataturn = await this.turnService.getTurns();
      return {
          list:dataturn
    }
}
}
