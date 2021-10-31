import { Controller, Get, Render, Req } from '@nestjs/common';
import { TurnService } from './turn.service';


@Controller('turn')
export class TurnController {
  constructor(private readonly turnService: TurnService) {}

    @Get()
    @Render('intro/index')
    async index() {
      var turn = await this.turnService.insertTurn(2,"def",false,"617e6b33bc3f80e9cd62ee7b");
      var list =  await this.turnService.getTurns();
      console.log(list);
    }
    @Get()
    async getAll(){

    }
    
    
}
