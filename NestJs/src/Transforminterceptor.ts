import { CallHandler, ExecutionContext, Injectable, Logger, NestInterceptor } from "@nestjs/common";
import { map } from "rxjs/operators";
import { Request } from "express";

@Injectable()
export class TransformInterceptor implements NestInterceptor {
    intercept(context: ExecutionContext, next: CallHandler) {
        console.log("拦截器前")
        const request = context.switchToHttp().getRequest() as Request;
        const startTime = Date.now();
        return next.handle().pipe(
            map((data) => {
                const endTime = Date.now();
                new Logger().log(`TIME:${endTime - startTime}\tURL:${request.path}\tMETHOD:${request.method}`)
                return {
                    data,
                };
            }),
        );
    }
    
}