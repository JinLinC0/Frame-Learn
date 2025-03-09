import { Body, Controller, Post } from '@nestjs/common';
import RegisterDto from './dto/register.dto';

@Controller('auth')
export class AuthController {
    @Post('register')
    register(@Body() dto: RegisterDto) {
        console.log(dto);
        return dto;
    }
}
