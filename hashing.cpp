#include <node.h>
#include <node_buffer.h>
#include <v8.h>
#include <stdint.h>

extern "C" {
    #include "keccak.h"
}

using namespace node;
using namespace v8;

// NODE_MAJOR_VERSION >=13

void keccak(const FunctionCallbackInfo<Value>& args) {
    v8::Isolate* isolate = args.GetIsolate();

    if (args.Length() < 1) {
        do {
            isolate->ThrowException(Exception::Error(String::NewFromUtf8(isolate, "You must provide one argument.").ToLocalChecked()));
            return;
        } while (0);
    }

	Local<Context> context = isolate->GetCurrentContext();

    Local<Object> target = args[0]->ToObject(context).ToLocalChecked();
    if(!Buffer::HasInstance(target)) {
        do {
            isolate->ThrowException(Exception::Error(String::NewFromUtf8(isolate, "Argument should be a buffer object.").ToLocalChecked()));
            return;
        } while (0);
    }

    char * input = Buffer::Data(target);
    char output[32];
    uint32_t input_len = Buffer::Length(target);

    keccak_hash(input, output, input_len);

    args.GetReturnValue().Set(Buffer::Copy(isolate, output, 32).ToLocalChecked());
}



void init(Local<Object> exports) {
    NODE_SET_METHOD(exports, "hash", keccak);
}


NODE_MODULE(hashing, init)
