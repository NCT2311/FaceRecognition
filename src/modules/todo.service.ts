import { Injectable } from '@nestjs/common';
import { InjectModel } from '@nestjs/mongoose';
import { Model } from 'mongoose';
import { Todo, TodoDocument } from '../models/todo.schema';

@Injectable()
export class TodoService {
  constructor(@InjectModel(Todo.name) private readonly model: Model<TodoDocument>) {}
}