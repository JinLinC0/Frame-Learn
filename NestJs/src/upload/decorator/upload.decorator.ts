import { applyDecorators, MethodNotAllowedException, UseGuards, UseInterceptors } from '@nestjs/common'
import { FileInterceptor } from '@nestjs/platform-express'
import { MulterOptions } from '@nestjs/platform-express/multer/interfaces/multer-options.interface'

// 对类型进行封装
export function fileFilter(type: string[]) {
    return (req: any, file: Express.Multer.File, callback: (error: Error | null, acceptFile: boolean) => void) => {
        console.log(file.mimetype)
        const check = type.some((t) => file.mimetype.includes(t))
        if(!check) {
            callback(new MethodNotAllowedException('文件类型错误'), false)
        } else {
            callback(null, true)
        }
    }
}

export function Upload(field='file', options: MulterOptions) {
  return applyDecorators(UseInterceptors(FileInterceptor(field, options)))
}

// 进一步分装实现专门用于图片的上传
export function UploadImage(field='file') {
    return Upload(field, {
        limits: { fieldSize: 1024 * 1024 * 3 },
        fileFilter: fileFilter(['image'])
    })
}

// 进一步分装实现专门用于文档的上传
export function UploadDocument(field='file', type: string[] = ['pdf', 'vnd.openxmlformats-officedocument.wordprocessingml.document']) {
    return Upload(field, {
        limits: { fieldSize: 1024 * 1024 * 3 },
        fileFilter: fileFilter(type)
    })
}