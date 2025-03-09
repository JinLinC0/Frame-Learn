import { ValidationError, ValidationPipe } from "@nestjs/common";

export class Validate extends ValidationPipe {
    protected mapChildrenToValidationErrors(
        error: ValidationError, 
        parentPath?: string
    ): ValidationError[]{
        // 对错误的验证消息进行处理
        const errors = super.mapChildrenToValidationErrors(error, parentPath);
        errors.map(error => {
            for (const key in error.constraints) {
                error.constraints[key] = error.property + '-' + error.constraints[key];
            }
        })
        return errors;
    }
}
