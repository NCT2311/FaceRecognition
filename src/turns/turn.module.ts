import { Module } from "@nestjs/common";
import {MongooseModule  } from "@nestjs/mongoose";
import { TurnController } from "./turn.controller";
import {Turnschema} from "./turn.model";
import { TurnService } from "./turn.service";

 
@Module({
    imports: [MongooseModule.forFeature([{name: 'Turns', schema: Turnschema}])],
    controllers:[TurnController],
    providers: [TurnService],
})
export class TurnModule{}