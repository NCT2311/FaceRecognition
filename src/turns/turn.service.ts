
import { InjectModel } from '@nestjs/mongoose';
import { Injectable } from '@nestjs/common';
import { Model } from 'mongoose';
import { Turn } from './turn.model';

@Injectable()
export class TurnService {
  private turns: Turn[] = [];

  constructor(
    @InjectModel('Turns') private readonly turnModel: Model<Turn>,
  ) {}

  async insertTurn(
    id: Number,
    urlimg: string,
    Status: Boolean,
    Personid: String,
  ) {
    const newTurn = new this.turnModel({
      id,
      urlimg,
      Status,
      Personid
    });
    const result = await newTurn.save();
    return result.id as string;
  }

  async editTurn(turn: Turn) {
    this.turnModel.updateOne(turn);
  }
  async getTurns(){
    const result  = await this.turnModel.find();
    //console.log(result);
    return [...result];
  }
}
