import { Controller, Post, UploadedFile, UseInterceptors } from '@nestjs/common';
import { TransformInterceptor } from 'src/Transforminterceptor';
import { UploadDocument, UploadImage } from './decorator/upload.decorator';

@Controller('upload')
@UseInterceptors(new TransformInterceptor())
export class UploadController {
    @Post('image')
    @UploadImage()
    image(@UploadedFile() file: Express.Multer.File) {
        return file
    }

    @Post('document')
    @UploadDocument()
    document(@UploadedFile() file: Express.Multer.File) {
        return file
    }
}
