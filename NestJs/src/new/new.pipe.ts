import { ArgumentMetadata, Injectable, PipeTransform } from '@nestjs/common';

@Injectable()
export class NewPipe implements PipeTransform {
  transform(value: any, metadata: ArgumentMetadata) {
    return metadata.metatype == Number ? +value : value;
  }
}
