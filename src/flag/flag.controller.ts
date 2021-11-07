import { Controller, Get, Render, Req } from '@nestjs/common';
import { FlagService } from './Flag.service';


@Controller('flag')
export class FlagController {
  constructor(private readonly FlagService: FlagService) {}

    @Get()
    @Render('intro/index')
    async index() {


    //   var Flag = await this.FlagService.getFlags();
    //   var a = Flag;
    //   console.log(Flag);
    }
    @Get()
    async getAll(){

    }
    
    
}
