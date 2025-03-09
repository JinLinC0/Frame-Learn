import { ArgumentsHost, BadRequestException, Catch, ExceptionFilter, HttpStatus } from '@nestjs/common';

@Catch()
export class ValidateExceptionFilter<T> implements ExceptionFilter {
  catch(exception: T, host: ArgumentsHost) {
      // 接收一下异常，获取http中的上下文
      const ctx = host.switchToHttp();
      // 获取一下响应对象
      const response = ctx.getResponse();
      // 对表单验证异常进行判断，异常来源于请求错误，格式化响应错误
      if (exception instanceof BadRequestException) {
          const responseObject = exception.getResponse() as any;
          // 返回的状态码是422
          return response.status(HttpStatus.UNPROCESSABLE_ENTITY).json({
              // 设置返回的状态码和消息
              code: HttpStatus.UNPROCESSABLE_ENTITY,
              message: responseObject.message.map((error) => {
                  const info = error.split('-')
                  return {field:info[0],message:info[1]}
              })
          })
      }
      // 如果不是表单异常，就响应以下的内容，返回的状态码是400
      response.status(400).json({})
  }
}