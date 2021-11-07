import { Controller, Get, Post, Render, Req } from '@nestjs/common';
import { TurnService } from './turn.service';
import { FlagService } from '../flag/flag.service';

@Controller('admin')
export class TurnController {
  constructor(private readonly turnService: TurnService,private readonly FlagService: FlagService) {}

    @Get()
    @Render('turn/index')
    async index() {
      // await this.turnService.insertTurn("2243255","ab",true);

    }
    @Post('/getdata')
    async getdata2() { 
      var listflag = await this.FlagService.getFlags();
      var list =  await this.turnService.getTurns();
      var index = list.length;
      var index1 = listflag.length;
      // console.log(list[index-1].urlimg);
      return {
        list: list[index-1],
        flag:  listflag[index1-1]
    }
  }
    
    
}
