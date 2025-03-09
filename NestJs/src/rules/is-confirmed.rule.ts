import { ValidationArguments, ValidatorConstraint, ValidatorConstraintInterface } from "class-validator";

@ValidatorConstraint()
export class IsConfirmed implements ValidatorConstraintInterface {
    // 进行密码比对
    async validate(value: string, args: ValidationArguments) {
        return value === args.object[args.property + '_confirmed'];
    }
    // 默认消息：比对失败的提示消息
    defaultMessage(args: ValidationArguments) {
        return '比对失败';
    }
}