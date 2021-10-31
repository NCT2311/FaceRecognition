
import { InjectModel } from '@nestjs/mongoose';
import { Injectable, NotFoundException } from '@nestjs/common';
import { Model, Schema } from 'mongoose';
import { Turn } from './turn.model';



@Injectable()
export class TurnService {
  private turns: Turn[] = [];

  constructor(
    @InjectModel('turns') private readonly turnModel: Model<Turn>,
  ) {}

  async insertTurn( urlimg: string,Personid: string, Status: Boolean  ) {
    const newTurn = new this.turnModel({
      urlimg,
      Personid,
      Status,
    });
    const result = await newTurn.save();
    return result.id as string;
  }

  async editTurn(
    turnId: string,
    urlimg: string,
    Status: Boolean,
  ) {
    const update =await this.turnModel.findById(turnId);
    update.Status = Status;
    update.urlimg = urlimg;
    update.save();
  }
  async getSingTurn(turnId: string){
    const result = await this.turnModel.findById(turnId);
    return {
      id: result.id,
      urlimg: result.urlimg,
      Personid: result.Personid,
      Status: result.Status,

    }
  }
  
  async getbyPersonID(a: String){
    const data = await this.turnModel.find();
    
    // console.log(result[0].Personid.toString());


    //chiêu cuối
    //  const data =  await this.getTurns();
    let result = new Array();
    for (var i = 0 ; i < data.length ; i++) {
      if (data[i].Personid.toString() == a){
        result.push(data[i]);
      }
    }
    return result;

  }
  async deleteTurn(turnId: string){
    await this.turnModel.deleteOne({_id: turnId}).exec();
  }
  async getTurns() {
    const turns = await this.turnModel.find().exec();
    //console.log(result);
    return turns.map((prod) => ({
      id: prod.id,
      urlimg: prod.urlimg,
      Personid: prod.Personid,
      Status: prod.Status,
    }));
  }

}
