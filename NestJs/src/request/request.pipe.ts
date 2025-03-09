import { ArgumentMetadata, HttpException, HttpStatus, Injectable, PipeTransform } from '@nestjs/common';
import { plainToInstance } from 'class-transformer';
import { validate } from 'class-validator';

@Injectable()
export class RequestPipe implements PipeTransform {
  async transform(value: any, metadata: ArgumentMetadata) {
    const object = metadata.metatype ? plainToInstance(metadata.metatype, value) : value;
    const errors = await validate(object);
    if (errors.length) {
      const message = errors.map((error) => ({
        name: error.property,
        message: Object.values(error.constraints ? error.constraints : {}).map((v) => v),
      }));
      throw new HttpException(message, HttpStatus.BAD_REQUEST);
    }
    console.log(object);
    return value;
  }
}


