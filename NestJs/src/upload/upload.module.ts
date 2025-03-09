import { Global, Module } from '@nestjs/common'
import { MulterModule } from '@nestjs/platform-express'
import { diskStorage } from 'multer'
import { extname } from 'path'
import { UploadController } from './upload.controller'
@Global()
@Module({
  imports: [
    // 系统提供的上传模块MulterModule
    MulterModule.registerAsync({
      useFactory() {
        return {
          storage: diskStorage({
            // 文件储存位置
            destination: 'uploads',
            // 文件名定制
            filename: (req, file, callback) => {
              // 时间戳加上随机数再加上文件后缀名
              const path = Date.now() + '-' + Math.round(Math.random() * 1e10) + extname(file.originalname)
              callback(null, path)
            },
          }),
        }
      },
    }),
  ],
  controllers: [UploadController],
})
export class UploadModule {}