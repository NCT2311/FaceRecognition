import { Controller, Get, Render, Req, UseGuards } from '@nestjs/common';
import { AuthGuard } from '@nestjs/passport';
import { FlagService } from './flag.service';


@Controller('flag')
export class FlagController {
  constructor(private readonly FlagService: FlagService) {}

    @Get()
    @UseGuards(AuthGuard('jwt'))
    @Render('new')
    async index() {


    //   var Flag = await this.FlagService.getFlags();
    //   var a = Flag;
    //   console.log(Flag);
    }

    
    
}
