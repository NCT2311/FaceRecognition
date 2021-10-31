import { Controller, Get, Render, Req } from '@nestjs/common';
import { TurnService } from './turn.service';


@Controller('turn')
export class TurnController {
  constructor(private readonly turnService: TurnService) {}

    @Get()
    @Render('intro/index')
    async index() {
      // await this.turnService.insertTurn("2243255","ab",true);
      var list =  await this.turnService.getbyPersonID("617e6b5c5ee18d0ef242a27d");
      console.log(list);
    }
    // @Get()
    // async getAll(){

    // }
    
    
}
