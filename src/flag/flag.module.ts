import { Module } from "@nestjs/common";
import {MongooseModule  } from "@nestjs/mongoose";
import { FlagController } from "./flag.controller";
import {Flagschema} from "./flag.model";
import { FlagService } from "./flag.service";

 
@Module({
    imports: [MongooseModule.forFeature([{name: 'Flags', schema: Flagschema}])],
    controllers:[FlagController],
    providers: [FlagService],
})
export class FlagModule{}  