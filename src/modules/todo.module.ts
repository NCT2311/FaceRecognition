import { Module } from '@nestjs/common';
// import { TodoService } from './todo.service';
// import { TodoController } from './todo.controller';
import { MongooseModule } from '@nestjs/mongoose';
import { Todo, TodoSchema } from '../models/todo.schema';

@Module({
  providers: [],
  controllers: [],
  imports: [
    MongooseModule.forFeature([{ name: Todo.name, schema: TodoSchema }]),
  ],
})
export class TodoModule {}