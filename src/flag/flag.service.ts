import { InjectModel } from '@nestjs/mongoose';
import { Injectable, NotFoundException } from '@nestjs/common';
import { Model } from 'mongoose';
import { Flag } from './flag.model';

@Injectable()
export class FlagService {
  private Flags: Flag[] = [];

  constructor(
    @InjectModel('Flags') private readonly FlagModel: Model<Flag>,
  ) {}

  async insertFlag( Flagcheck: Boolean) {
    const newFlag = new this.FlagModel({
        Flagcheck
    });
    const result = await newFlag.save();
    return result.id as string;
  }

  async editFlag(
      id:string,
    Flagcheck: Boolean,
  ) {
    const update =await this.FlagModel.findById(id);
    update.Flagcheck = Flagcheck;
    update.save();
  }
  async getSingFlag(FlagId: string){
    const result = await this.FlagModel.findById(FlagId);
    return {
      Flagcheck: result.Flagcheck,

    }
  }
  async deleteFlag(FlagId: string){
    await this.FlagModel.deleteOne({_id: FlagId}).exec();
  }
  async getFlags() {
    const Flags = await this.FlagModel.find().exec();
    //console.log(result);
    return Flags.map((prod) => ({
      Flagcheck: prod.Flagcheck,
    }));
  }
  // private async findFlag(id: string): Promise<Model<Flag>> {
  //   let Flag;
  //   try{
  //     Flag = await this.FlagModel.findById(id);
  //   } catch(error){
  //     throw new NotFoundException('khong tim thay');
  //   }
  //   if(!Flag) throw new NotFoundException('khong tim thay');
  //   return Flag;
  // }
}
