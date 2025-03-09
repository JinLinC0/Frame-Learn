import { PartialType } from "@nestjs/mapped-types";
import RegisterDto from "./register.dto";
import { Validate } from "class-validator";

// 继承注册的dto，将其类型都变成可选项
export default class Login2Dto extends PartialType(RegisterDto){}